import * as React from 'react';
import { Text, View, StyleSheet, Image } from 'react-native';
import { Avatar, Button, Card, Title, Paragraph } from 'react-native-paper';
export default function AssetExample() {
  return (


    <View style={styles.subcontainer}>
            <Text style={styles.menuitem}>Новости</Text>
        <Text style={styles.aritcleheader}>Превращаем стресс в своего помощника</Text>
    <Image style={styles.logo} source={require('../assets/download1.jpg')} />
    
      <Text style={styles.paragraph}>
        Исследователи Йельского университета заявляют, что люди, которые рассматривают стресс, как возможность личностного роста, отмечают улучшение качества жизни. Сегодня узнаем, как это работает и как увидеть положительные стороны стресса.
      </Text>

    </View>

  );
}

const styles = StyleSheet.create({
  subcontainer: {
    borderRadius: 5,
    backgroundColor: 'white',
    padding: 15,
    margin: 5,
  },
  paragraph: {
    marginTop: 0,
    fontSize: 14,
    fontWeight: 'bold',

  },
  logo: {
    height: 128,
    width: 214,
    marginBottom: 30,
  },

  
  aritcleheader: {
    color: 'black',
    fontWeight: 'bold',
    fontSize: 18,
    marginBottom: 30,
  },

  menuitem:{
    marginTop: 15,
    textAlign: 'left',
    color: "blue",
    marginBottom: 15,

  }
});
