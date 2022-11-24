import * as React from 'react';
import { Text, View,Image, StyleSheet, Pressable, Button, TouchableOpacity, ImageBackground, Dimensions, Alert } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Constants from 'expo-constants';
import ShareExample from './share'
import {Linking} from 'react-native'


const Stack = createNativeStackNavigator();

const Contacts = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{ title: 'Cписок контактов' }}
        />
        <Stack.Screen 
        name="Profile" 
        component={ProfileScreen} 
        />
        <Stack.Screen 
        name="Call" 
        component={CallScreen} 
        />
        <Stack.Screen 
        name="VideoCall" 
        component={VideoCallScreen} 
        /> 
      </Stack.Navigator>
    </NavigationContainer>
  );
};


const HomeScreen = ({ navigation }) => {


  return (
    <View>
      <Pressable 
        onPress={() =>
          navigation.navigate('Profile', { name: 'Дмитрий Автосервис', photo: 'https://sun9-43.userapi.com/impg/3gzVxC9sKOJmsry9YxtqEQBZfozUDTY4u02G7g/1nolOIUSUy4.jpg?size=740x555&quality=95&sign=17b084b82feee206267061a536596f8a&type=album', phone: "0109876652" })
        }
        style={styles.button}
      >
      <View style={styles.container}>
        <Image style = {styles.picture}
        source={{
          uri: 'https://sun9-43.userapi.com/impg/3gzVxC9sKOJmsry9YxtqEQBZfozUDTY4u02G7g/1nolOIUSUy4.jpg?size=740x555&quality=95&sign=17b084b82feee206267061a536596f8a&type=album',
        }}
        />
         <Text style={styles.text}>Дмитрий Автосервис</Text>
         </View>
      </Pressable>

      <Pressable 
        onPress={() =>
          navigation.navigate('Profile', { name: 'Рома колледж', photo: 'https://i.pinimg.com/originals/b0/6d/f9/b06df9b8d314c6ae9c596602b6254af8.jpg', phone: "0105567652" })
        }
        style={styles.button}
      >
         <View style={styles.container}>
        <Image style = {styles.picture}
        source={{
          uri: 'https://i.pinimg.com/originals/b0/6d/f9/b06df9b8d314c6ae9c596602b6254af8.jpg',
        }}
        />
         <Text style={styles.text}>Рома колледж</Text>
         </View>
      </Pressable>

      <Pressable 
        onPress={() =>
          navigation.navigate('Profile', { name: 'Кузя запчасти ВЫХИНО', photo: 'https://sun9-76.userapi.com/impg/j_W9yTDzIOUI-ttnIDGl72HIf9B_r9LUGMIs-g/8YhgJlQ8F5Y.jpg?size=540x303&quality=95&sign=dcd5f3fff29dafb356d2421eab967720&type=album', phone: "01096787652" })
        }
        style={styles.button}
      >
          <View style={styles.container}>
        <Image style = {styles.picture}
        source={{
          uri: 'https://sun9-76.userapi.com/impg/j_W9yTDzIOUI-ttnIDGl72HIf9B_r9LUGMIs-g/8YhgJlQ8F5Y.jpg?size=540x303&quality=95&sign=dcd5f3fff29dafb356d2421eab967720&type=album',
        }}
        />
         <Text style={styles.text}>Кузя запчасти ВЫХИНО</Text>
         </View>
      </Pressable>

      <Pressable 
        onPress={() =>
          navigation.navigate('Profile', { name: 'Грузинская кухня Яснево', photo: 'https://sun9-31.userapi.com/impg/Vvq8PVVZ1FJnQESi5ze0S9rsnO0JO8Ck7rQsQg/nHn25J0CkJI.jpg?size=665x1000&quality=95&sign=84b455e4b4e1891b144517243c2df9a7&type=album', phone: '+799952992529' })
        }
        style={styles.button}
      >
          <View style={styles.container}>
        <Image style = {styles.picture}
        source={{
          uri: 'https://sun9-31.userapi.com/impg/Vvq8PVVZ1FJnQESi5ze0S9rsnO0JO8Ck7rQsQg/nHn25J0CkJI.jpg?size=665x1000&quality=95&sign=84b455e4b4e1891b144517243c2df9a7&type=album',
        }}
        />
         <Text style={styles.text}>Грузинская кухня Яснево</Text>
         </View>
      </Pressable>
      </View>

  );
};

const ProfileScreen = ({ navigation, route }) => {
  return (
  <View style={styles.profile}>
      <Image style = {styles.profilePicture}
        source={{
          uri: route.params.photo,
        }}
        />
      <Text style={styles.profileText}>{route.params.name}</Text>
      <Text style={styles.phoneNumber}> {route.params.phone} </Text> 

      <View style={styles.actionContainer}>
    
        <TouchableOpacity  style={{flex: 1}}
          onPress={() => Linking.openURL("tel:"+route.params.phone)

          }>

          <Image style = {styles.icon}
                  source={{
                  uri: 'https://sun9-24.userapi.com/impg/IZciE5BzErQXOTPCYHeRVMFrQGYuT1jkPeyJ_Q/Kl5gttw5xSI.jpg?size=128x129&quality=95&sign=7fc1e3ce0c6eab7372338f150d954b08&type=album',
                  }}
                />
        </TouchableOpacity>


        <TouchableOpacity  style={{flex: 1}}
          onPress={() => Linking.openURL("sms:"+route.params.phone)

          }>

          <Image style = {styles.icon}
                  source={{
                  uri: 'https://sun9-60.userapi.com/impg/nbvYMUUT1QoakRrTiQ0abqeDZFJqdeXfv3cuiA/o_zUh8Q6w5I.jpg?size=126x126&quality=95&sign=aac187ab399f5a135ca24b80448b79c4&type=album',
                  }}
                />
        </TouchableOpacity>

        <TouchableOpacity  style={{flex: 1}}
          onPress={() =>
            navigation.navigate('VideoCall', {name: route.params.name, photo: route.params.photo, phone: route.params.phone})
          }>
          <Image style = {styles.icon} 
            source={{
            uri: 'https://sun9-46.userapi.com/impg/oCSyIQlxo-yh3cPzx8_j9vgJ4vGln5v6tm4cDA/GOJT88kNPos.jpg?size=126x126&quality=95&sign=c648c8aa3665ac0b6ad7ff446752f9ef&type=album',
            }}
          />
        </TouchableOpacity >
        

      </View>
            <ShareExample title={route.params.name+" "+route.params.phone}/>

    </View> 
     
)};

const CallScreen = ({ navigation, route }) => {
  return (
      <ImageBackground style={{ flex: 1}} 
        source={{
          uri: route.params.photo,
        }}>
        <View style={{alignItems: "center", justifyContent: "center", flex: 1, backgroundColor: 'rgba(1,1,1,0.7)'}}>
          <Image style={{width: 150, height: 150, borderRadius: 100}} source={{uri:route.params.photo}}/>
          <Text style={{textAlign: "center", fontSize:28, color:"rgb(255,255,255)", fontWeight: "bold"}}>
           Calling {route.params.name}...
          </Text>
          <Text style={{textAlign: "center", fontSize:20, color:"rgb(255,255,255)"}}>{route.params.phone}</Text>
          <TouchableOpacity 
            onPress={() =>
            navigation.navigate('Profile', {name: route.params.name, photo: route.params.photo, phone: route.params.phone})
            }>
          <Image style={{width: 50, height: 50, marginTop: 150}} source={{uri: "https://i.ya-webdesign.com/images/red-phone-icon-png-8.png"}}/>
        </TouchableOpacity>
        </View>
      </ImageBackground>
     
)};

const VideoCallScreen = ({ navigation, route }) => {
  return (
      <ImageBackground style={{ flex: 1}} 
        source={{
          uri: route.params.photo,
        }}>
        <View style={{alignItems: "center", justifyContent: "center", flex: 1, backgroundColor: 'rgba(1,1,1,0.7)'}}>
          <Image style={{width: 150, height: 150, borderRadius: 100}} source={{uri:route.params.photo}}/>
          <Text style={{textAlign: "center", fontSize:28, color:"rgb(255,255,255)", fontWeight: "bold", marginLeft: 20, marginRight: 20}}>
           Starting a video call with {route.params.name}...
          </Text>
          <Text style={{textAlign: "center", fontSize:20, color:"rgb(255,255,255)"}}>{route.params.phone}</Text>
          <TouchableOpacity 
            onPress={() =>
            navigation.navigate('Profile', {name: route.params.name, photo: route.params.photo, phone: route.params.phone})
            }>
          <Image style={{width: 50, height: 50, marginTop: 150}} source={{uri: "https://i.ya-webdesign.com/images/red-phone-icon-png-8.png"}}/>
        </TouchableOpacity>
        </View>
      </ImageBackground>
     
)};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'row',
    backgroundColor: "rgb(255, 255, 255)"
  },
  profile:{
    marginTop: 20,
    alignItems: "center",
    backgroundColor: "rgb(255, 255, 255)",
    borderRadius: 20
  },
  button: {
    height: 80,
    backgroundColor : "rgb(250, 250, 250)",
    borderRadius: 8,
    borderColor: "rgb(1,1,1)",
    margin: 1
  },
  text: {
    fontSize: 18,
    lineHeight: 21,
    fontWeight: 'bold',
    marginLeft: 20,
    marginTop: 30
  },
  picture: {
    marginTop: 15,
    marginLeft: 15,
    width: 50,
    height: 50,
    borderRadius: 100
  },
  profilePicture: {
    marginTop: 20,
    width: 150,
    height: 150,
    borderRadius: 10
  },
  profileText: {
    fontSize: 32,
    fontWeight: 'bold',
    marginTop: 20
  },
  phoneNumber: {
    fontSize: 20
  },
  icon: {
    marginTop: 15,
    marginLeft: 20,
    marginRight: 20,
    width: 30,
    height: 30,
    borderRadius: 100,
    marginBottom: 30
  },
  actionContainer: {
    marginRight: 80,
    marginLeft: 80,
    alignItems: 'center',
    flexDirection: "row",
    justifyContent: "center"
  }
});


export default Contacts;
