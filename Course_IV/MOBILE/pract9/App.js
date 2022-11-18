import * as React from 'react';
import { Text, View, StyleSheet, Image, Button, Platform } from 'react-native';

import { addMultipleGifs, deleteAllGifs, getSingleGif } from './GifManagement';


// those are Giphy.com ID's - they are hardcoded here,
// but if you have Giphy API key - you can use findGifs() from gifFetching.ts

function randomIntFromInterval(min, max) { // min and max included 
  return Math.floor(Math.random() * (max - min + 1) + min)
}

const getItemsGIF = async () => {
  try {
    const response = await fetch(
      'https://api.giphy.com/v1/gifs/trending?api_key=SOME_KEY'
    );
    const json = await response.json();

    let randomIndex = randomIntFromInterval(0, 45);
    result =  "https://media.giphy.com/media/"+json.data[randomIndex]["id"]+"/giphy.gif"

    console.log(result)
    return result
  } catch (error) {
    console.error(error);
  }
};


function AppMain() {

  


  //let response = getItemsGIF();
  //console.log(response)


  let gifIds = []


  //download all gifs at startup
  React.useEffect(() => {
    (async () => {
      await addMultipleGifs(gifIds);
    })();

    //and unload at the end
    return () => {
      deleteAllGifs();
    };
  }, []);

  //file uri of selected gif
  const [selectedUri, setUri] = React.useState(null);

  const handleSelect = async id => {
    try {
      setUri(await getItemsGIF());
    } catch (e) {
      console.error("Couldn't load gif", e);
    }
  };

  const unloadAll = () => {
    setUri(null);
    deleteAllGifs();
  };



  return (

    <View style={styles.container}>
      <Text style={styles.header}>See contents of gifManagement.ts</Text>
      <Text style={styles.paragraph}>Select one of the IDs</Text>

      <Button title={`Random gif`} onPress={() => handleSelect(0)} />


      <Button title="Unload all" onPress={unloadAll} />

      <Text style={styles.paragraph}>Selected URI: {selectedUri || 'none'}</Text>
      {selectedUri != null && <Image style={{ height: 200 }} source={{ uri: selectedUri }} />}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 20,
    justifyContent: 'center',
    backgroundColor: '#ecf0f1',
    padding: 8,
  },
  header: {
    margin: 24,
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  paragraph: {
    textAlign: 'center',
    marginBottom: 15,
  },
});

function UnsupportedPlatform() {
  return (
    <View style={styles.container}>
      <Text style={styles.header}>
        FileSystem doesn&#39;t support web. Run this on Android or iOS
      </Text>
    </View>
  );
}

export default function App() {
  return Platform.OS === 'android' || Platform.OS === 'ios' ? <AppMain /> : <UnsupportedPlatform />;
}
