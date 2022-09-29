import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';

const FlexDimensionsBasics = () => {
  return (
    <View style={styles.baseview}>
      <View style={styles.baseview}>
        <Text style={[styles.text, styles.bold]}>
          Излишек средств банков в ЦБ достиг годового максимума
        </Text>
      </View>
      <View style={styles.view2}>
        <Text style={[styles.text, styles.font]}>
          С чем связан резкий рост профицита ликвидности
        </Text>
      </View>
      <View style={styles.view3}>
        <Text style={styles.text}>
Российские банки к середине сентября существенно нарастили чистые требования к Центробанку: структурный профицит ликвидности банковского сектора на 14 сентября достиг 3,66 трлн руб. — максимального уровня с августа 2021 года, следует из статистики регулятора. С начала недели показатель увеличился на 22,2%.
        </Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  baseview: {
    flex: 1,
    backgroundColor: '#FFF',
    padding: 'auto',
  },
  view2: {
    flex: 1,
    backgroundColor: '#e5e5e5',
  },
  view3: {
    flex: 6,
    backgroundColor: '#aaa',
  },
  text: {
    margin: 'auto',
    justifyContent: 'center',
    textAlign: 'center',
    paddingStart: '5%',
    paddingEnd: '5%',
  },
  bold: {
    fontWeight: 'bold',
  },
  font: {
    fontSize: '15',
  },
});

export default FlexDimensionsBasics;
