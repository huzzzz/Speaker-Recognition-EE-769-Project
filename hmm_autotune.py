import librosa
import numpy as np
import librosa.display
from hmmlearn import hmm
import os
import warnings
import pickle

warnings.filterwarnings("ignore")

#Number of states per HMM
N = 50

#Num of speaker
Num_Speakers = 10

#number of utts to take per speaker
num_file_per_speaker = 10


def mfcc_module(data):
	y , sr = librosa.load(data , sr=None)
	mfcc = librosa.feature.mfcc(y=y, sr=sr,n_mfcc=13,hop_length=int(0.010*sr), n_fft=int(0.025*sr))
	mfcc_delta =  librosa.feature.delta(mfcc,order =1)
	mfcc_double_delta =  librosa.feature.delta(mfcc,order =2)
	array = np.append(mfcc,mfcc_delta,axis=0)
	array = np.append(array,mfcc_double_delta,axis=0)
	return array.T

def get_final_feature(id):
	lens = []
	features = []
	i = 0
	for file in os.listdir("train/"+str(id)):
		if i > num_file_per_speaker :
			break
		i +=1
		curr_feat = mfcc_module("train/"+str(id)+"/"+file)
		curr_feat = list(curr_feat)
		features += curr_feat
		lens.append(len(curr_feat))
	out = np.array(features)
	return out,lens

def create_model(n_states,id):
	if ("model" + str(id)) in os.listdir("Models"):
		return pickle.load(open('Models/model'+str(id) ,'wb'))
	features , lens = get_final_feature(id)
	model = hmm.GaussianHMM(n_components=N, covariance_type="diag", init_params='mcs', params='mcs', n_iter=10, 
							tol=1e-7, verbose=True)
	model.transmat_ = np.ones((N, N), dtype='float') / N
	model.fit(features,lens)
	pickle.dump(model,open('Models/model'+str(id) ,'wb'))
	return model

np.random.seed(42)
id_list = os.listdir("./train")
speaker_list = []
model_list = []
num = 0
print("id list :",id_list)

for i in id_list :
	if num > Num_Speakers:
		break
	num +=1
	my_id = int(i)
	model_list.append([create_model(N,my_id),my_id])
	speaker_list.append(my_id)

print("speaker :",speaker_list)
actual_list = []
pred_list = []

test_limit = 1

for i in id_list:
	if int(i) in speaker_list:
		test_num =0
		for j in os.listdir("./test/"+i):
			if test_num >= test_limit :
				break
			test_num += 1
			max_score = -float('inf')
			index = 0
			for k in range(len(model_list)):
				score = model_list[k][0].score(mfcc_module("test/"+i+"/"+j)[:200,:])
				if max_score < score:
					index = j
					max_score = k
			print("i is :",i)
			pred_list.append(model_list[index][1])
			actual_list.append(int(i))

print("pred list :",pred_list)
print("actual list :",actual_list)

count = 0.0
for i in range(0,len(actual_list)):
    if actual_list[i] == pred_list[i]:
    	count += 1

print(((count*1.0)/len(actual_list))*100)
	
