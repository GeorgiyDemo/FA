import * as React from 'react';
import { WebView } from 'react-native-webview';
import { StyleSheet } from 'react-native';
import Constants from 'expo-constants';

import {StatusBar} from 'react-native';

export default class App extends React.Component {
   render() {
      return <>
       <StatusBar backgroundColor={"black"} />                  
       <WebView source={{ uri: 'https://georgiydemo.github.io/' }} style={styles.container} />
       </>;
   }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: Constants.statusBarHeight,
    backgroundColor: "black",
  },
});
