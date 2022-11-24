import React from "react";
import * as Font from "expo-font";
import AppNavigator from "./src/navigations/Navigator";
import * as SplashScreen from "expo-splash-screen";

export default class App extends React.Component {
  state = {
    appIsReady: false,
  };

  // Using expo-splash-screen cause expo-app-loading is deprecated in favor of expo-splash-screen
  async componentDidMount() {
    try {
      await SplashScreen.preventAutoHideAsync();

      await Font.loadAsync({
        Bold: require("./src/fonts/Montserrat-ExtraBold.otf"),
        Medium: require("./src/fonts/Montserrat-Medium.otf"),
        Regular: require("./src/fonts/Montserrat-Regular.otf"),
      });
    } catch (e) {
      console.warn(e);
    } finally {
      this.setState({ appIsReady: true });
    }

    if (this.state.appIsReady) {
      await SplashScreen.hideAsync();
    }
  }
  render() {
    return this.state.appIsReady === true ? <AppNavigator /> : null;
  }
}



