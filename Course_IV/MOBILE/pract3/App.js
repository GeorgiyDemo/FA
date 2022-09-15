import AssetExample from './components/AssetExample';


import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
const LotsOfStyles = () => {
    return (
      <View style={styles.container}>
       <Text style={styles.header}>Журнал Bright</Text>
       <AssetExample/>
      </View>
    );
};
const styles = StyleSheet.create({

  container: {
    paddingTop: 40,
    backgroundColor: '#edf0f0',
    height: '100%'
  },

  header: {
    textAlign: 'center',
    fontWeight: 'bold',
    fontSize: 16,
    marginTop: 0,
  },
});
export default LotsOfStyles;

