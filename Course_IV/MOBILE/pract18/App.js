import React, { useState, useEffect } from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';
import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import { createBottomTabNavigator } from 'react-navigation-tabs';

function HomeScreen() {
  const [studentItems, setStudentItems] = useState([]);

  const fetchStudentItems = async () => {
    const response = await fetch('https://63a439dc821953d4f2ad9a62.mockapi.io/api/Item');
    const data = await response.json();
    setStudentItems(data);
  };

  useEffect(() => {
    fetchStudentItems();
  }, []);

  return (
    <View style={styles.container}>
      <FlatList
        data={studentItems}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={styles.item}>
            <Text style={styles.name}>{item.name}</Text>
            <Text style={styles.email}>{item.email}</Text>
            <Text style={styles.grades}>Grades:</Text>
            {item.grades.map((grade) => (
              <Text key={grade.course} style={styles.grade}>
                {grade.course}: {grade.grade}
              </Text>
            ))}
          </View>
        )}
      />
    </View>
  );
}

HomeScreen.navigationOptions = {
  title: 'Home',
};

function SettingsScreen() {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Settings Screen</Text>
    </View>
  );
}

SettingsScreen.navigationOptions = {
  title: 'Settings',
};

const AppStack = createStackNavigator({
  Home: { screen: HomeScreen },
});

const AppNavigator = createBottomTabNavigator({
  Home: { screen: AppStack },
  Settings: { screen: SettingsScreen },
});

const AppContainer = createAppContainer(AppNavigator);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  item: {
    padding: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
  },
  name: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  email: {
    fontSize: 14,
    color: '#666',
  },
  grades: {
    fontSize: 16,
    fontWeight: 'bold',
    marginTop: 10,
  },
  grade: {
    fontSize: 14,
    marginTop: 5,
  },
});

export default AppContainer;
