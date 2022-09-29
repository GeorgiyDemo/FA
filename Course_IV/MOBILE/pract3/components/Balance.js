import * as React from 'react';
import { Text, View, StyleSheet, Image } from 'react-native';

export default function Balance() {
  return (
    <View style={styles.container}>
      <Text ><b>Текущий баланс:</b> 454,91 руб</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
    padding: 24,
  },
});
