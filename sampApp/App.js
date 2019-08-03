import React, {Fragment} from 'react';
import {
  SafeAreaView,StyleSheet,View,Text,Image,StatusBar, TouchableOpacity
} from 'react-native';

import Ionicon from 'react-native-vector-icons/Ionicons';
import { Button } from 'react-native-elements';

import Tts from 'react-native-tts';
import Voice from 'react-native-voice';
import axios from 'react-native-axios';
//import AnimatedLoader from 'react-native-animated-loader';

import Logo from './assets/logo_dark.jpeg';

export default class App extends React.Component {
  state = {
    active: false,
    res: "",
    rep: ""
  }
  componentDidMount(){
    Voice.onSpeechStart = this.onSpeechStart;
    Voice.onSpeechRecognized = this.onSpeechRecognized;
    Voice.onSpeechEnd = this.onSpeechEnd;
    Voice.onSpeechError = this.onSpeechError;
    Voice.onSpeechResults = this.onSpeechResults;
  }
  componentWillUnmount(){
      Voice.destroy().then(Voice.removeAllListeners);
  }
  onSpeechStart = () => {
    this.setState({
      active: true
    })

  }
  onSpeechRecognized = rec => {
    //rec
  };
  onSpeechError = err => {
    alert(JSON.stringify(err.error))
  };
  onSpeechResults = (result) => {
    this.setState({
      res: result.value[0],
    });

    let formData = new FormData()
    formData.append("utext", this.state.res)
    if(this.state.res.includes("launch"))
      this.setState({
        rep: "Launching Bot"
      })
    axios({
      method: "POST",
      url: "http://192.168.43.218:5000/botResponse",
      data: formData,
      config: { headers: {'Content-Type': 'multipart/form-data' }}
    })
    .then(res => {
      this.setState({
        rep: res.data.response
      })
    })

  };
  onSpeechEnd = () => {
    this.setState({
      active: false
    })
  }
  _start = async () => {
    this.setState({
      res: "",
      rep: ""
    })
    try {
      await Voice.start('en-US');
    } catch (e) {
      alert(e)
    }
  }
  _stop = async () => {
    try {
      await Voice.stop();
    } catch (e) {
      alert(e)
    }
  }
  speak = () => {
    Tts.speak(this.state.rep)
  }
  render(){
    if(this.state.rep != ""){
      this.speak()
    }
    return (
        <SafeAreaView style={styles.container}>
          <View style={{justifyContent: 'center', height: "30%"}}>
            <Image source={Logo} style={styles.logo} />
          </View>
          <View style={{justifyContent: 'space-evenly', height: "70%", width: "100%", alignItems: 'center'}}>
            <Text style={[styles.textStyle, {fontSize: 22.5}]}>User Input: {this.state.res}</Text>
            <Text style={styles.textStyle}>{this.state.active ? "Active" : "Inactive"}</Text>
            <TouchableOpacity onPress={this._start} style={styles.buttonStyle}>
              <Ionicon name="md-mic" size={30} style={{padding: 15}} color="#FFFFFF"/>
            </TouchableOpacity>

            <Text style={[styles.textStyle, {fontSize: 22.5}]}>Reply: {this.state.rep}</Text>
          </View>
        </SafeAreaView>
    );
    //<Button title="Stop" onPress={this._stop}/>
    //<Image source={{uri: "https://media.giphy.com/media/vd8bWznL362DC/giphy.gif"}} style={{width: 100, height: 100}} />

  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#000000",
    justifyContent: 'space-evenly',
    alignItems: 'center',
  },
  logo: {
    width: 300,
    height: 250,
  },
  textStyle: {
    fontSize: 25,
    fontWeight: "bold",
    color: "#FFFFFF"
  },
  buttonStyle: {
    backgroundColor: "blue",
    borderRadius: 30
  },
  lottie: {
    width: 100,
    height: 100,
  }
});
