import * as React from 'react';
import { Text, View, StyleSheet, Image, ImageButton, Button } from 'react-native';

export default function NextButton() {
  return (
  <View >
    <Button
      style={styles.button}
      title="Скрыть данные"/>
  </View>
  );
}

const styles = StyleSheet.create({
  button: {
    flex: 1,
    justifyContent: 'flex-end',
    alignSelf: "stretch",
    marginBottom: 36
  }

  

});
