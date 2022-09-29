import * as React from 'react';
import { Text, View, StyleSheet, Image, FlatList} from 'react-native';

export default function Article() {
  return (
    <View style={styles.container}>
      <FlatList
        data={[
          {key: 'Номер карты: 548543868346'},
          {key: 'Действительна до: 09/31'},
          {key: 'CVV: 241'},
        ]}
        
        renderItem={({item}) => <Text style={styles.item}>{'\u2B24' + ' '}{item.key}</Text>}
      />

    </View>
  );
}

const styles = StyleSheet.create({
  container: {
   flex: 1,
   paddingTop: 10,
   paddingBottom: 10,
  },
  item: {
    padding: 5,
  },
  
});
