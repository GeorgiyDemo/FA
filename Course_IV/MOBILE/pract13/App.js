import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity, TextInput } from 'react-native';
import * as SQLite from 'expo-sqlite';

const db = SQLite.openDatabase('todo.db');

const App = () => {
  const [todo, setTodo] = useState('');
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    db.transaction(tx => {
      tx.executeSql(
        'create table if not exists todo (id integer primary key not null, todo text);'
      );
    });
    updateList();
  }, []);

  const addTodo = () => {
    db.transaction(
      tx => {
        tx.executeSql('insert into todo (todo) values (?)', [todo]);
      },
      null,
      updateList
    );
  };

  const deleteTodo = id => {
    db.transaction(
      tx => {
        tx.executeSql(`delete from todo where id = ?;`, [id]);
      },
      null,
      updateList
    );
  };

  const updateList = () => {
    db.transaction(tx => {
      tx.executeSql('select * from todo', [], (_, { rows }) =>
        setTodos(rows._array)
      );
    });
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        onChangeText={text => setTodo(text)}
        value={todo}
      />
      <TouchableOpacity style={styles.button} onPress={addTodo}>
        <Text style={styles.buttonText}>Add Todo</Text>
      </TouchableOpacity>
      <FlatList
        style={styles.list}
        keyExtractor={item => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.listItem}>
            <Text>{item.todo}</Text>
            <TouchableOpacity onPress={() => deleteTodo(item.id)}>
              <Text style={styles.deleteButton}>Delete</Text>
            </TouchableOpacity>
          </View>
        )}
        data={todos}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 30,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ddd',
    padding: 10,
    fontSize: 18,
    borderRadius: 6,
  },
  button: {
    backgroundColor: '#0066cc',
    padding: 10,
    margin: 10,
    alignItems: 'center',
borderRadius: 6,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
  },
  list: {
    marginTop: 20,
  },
  listItem: {
    borderColor: '#ccc',
    borderWidth: 1,
    padding: 10,
    marginBottom: 10,
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  deleteButton: {
    color: '#0066cc',
    fontSize: 18,
  },
});

export default App;
