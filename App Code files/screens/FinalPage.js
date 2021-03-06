import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  Text,
  View,
  Image,
  ListView,
  ScrollView,
  TextInput,
  TouchableOpacity,
  TouchableHighlight,
  Button
} from 'react-native';
import Toast from 'react-native-simple-toast';
import { NavigationActions } from 'react-navigation';

export default class FinalPage extends Component {
  render() {
    var final = this.props.navigation.state.params.final 
      return (
        <View style={styles.content}>
          <Text style={styles.welcome}>{final}</Text>
        </View>
      );
  }
}

const styles = {
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  input: {
    fontSize: 18,
    height: 60,
    borderColor: 'gray',
    backgroundColor: '#fff',
    borderWidth: 1,
    padding : 10,
    margin : 20,
    borderRadius: 10,

  },
  welcome: {
    fontSize: 20,
    color: '#2e2f30',
    textAlign: 'center',
    // marginTop: 10,
    // marginBottom: 10,
    backgroundColor: '#fff',
    padding: 20
  },
  maincontent: {
    marginTop: 10,
    alignItems:'center'
  },
  rightContainer : {
    flex:1,
    justifyContent: 'center'
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
  content:{
      flex:1,
  },
  submit: {
      margin: 20 ,
        alignSelf:'center',
        padding: 10,
        backgroundColor: '#4c83db',
      borderWidth: 1,
      borderRadius: 10,
        width: 250 
    },
  containerStyle: {
    flexDirection: 'row',
    flex: 1,
    // borderBottomWidth: 1,
    // borderColor: '#e2e2e2',
    justifyContent: 'flex-start',
    alignItems:'center',
    padding: 10,
    paddingLeft: 15,
    backgroundColor: '#fff',
    // marginBottom:5
  },
  description : {
    // flexDirection: 'row',
    // flex: 1,
    borderBottomWidth: 1,
    borderColor: '#e2e2e2',
    // justifyContent: 'flex-start',
    alignItems:'center',
    paddingBottom: 10,
    paddingLeft: 15,
    backgroundColor: '#fff',
    // marginBottom:10
  },
  imageStyle: {
    // width: 100, 
    // height: 100, 
    // marginRight: 20
    width:300,
    height:300,
    alignSelf:'center',
    alignItems:'center',
    backgroundColor: '#fff',
  },
  textStyle: {

    flex: 1,
    flexDirection: 'row',
    justifyContent: 'flex-start',
    // alignItems: 'center'
  },
  title: {
     color: '#2e2f30',
     marginRight: 10
  },
  author:{
    color: '#2e2f30'
  },
  totalStyle: {
    alignItems: 'center',
    marginTop: 3,
    borderRadius: 3
  },
};
