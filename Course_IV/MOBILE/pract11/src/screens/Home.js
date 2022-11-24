import React from 'react';
import {View,Text,Image,ImageBackground,TouchableOpacity} from 'react-native';
import {ScrollView,TextInput} from 'react-native-gesture-handler';
import Icon from '@expo/vector-icons/Entypo';
import Posts from '../screens/Posts'

export default class Home extends React.Component{
  
    state={
        popularSelected:true
    }
    onTabPressed=()=>{
        this.setState({popularSelected:!this.state.popularSelected})
    }
    render(){
        return(
          <ScrollView
            showsVerticalScrollIndicator={false}
            style={{
                height:"100%",
                backgroundColor:"#4969c2"
            }}
          >
              <View style={{
                  height:260,
                  width:"100%",
                  paddingHorizontal:35
              }}>
                  <View style={{
                      flexDirection:"row",
                      width:"100%",
                      paddingTop:40,
                      alignItems:"center"
                  }}>
                      <View style={{
                          width:"50%"
                      }}>
                          <Image source={require('../images/Untitled.png')}
                            style={{width:20,height:20}}/>
                      </View>
                      <View style={{
                          width:"50%",
                          alignItems:"flex-end",
                      }}>
                          <Icon name = "dots-two-vertical"
                            size={22}
                            color="#d2d2d2"
                            style={{
                                marginRight:-7,
                                marginTop:7
                            }}/>
                      </View>
                  </View>


                <Text style={{
                    fontFamily:"Bold",
                    fontSize:25,
                    color:"#FFF",
                    paddingVertical:25
                }}>Поиск великолепных фотографий</Text>

                <View style={{
                    flexDirection:"row",
                    borderColor:"#9ca1a2",
                    borderRadius:20,
                    borderWidth:0.2,
                    paddingVertical:5,
                    alignItems:"center"
                }}>
                    <TextInput
                        placeholder="Поиск вдохновения ..."
                        style={{
                            paddingHorizontal:20,
                            fontFamily:"Medium",
                            fontSize:11,
                            width:"90%",
                            color:"#9ca1a2"
                        }}
                    />
                    <Icon name="magnifying-glass"
                          size={15}
                          color="#9ca1a2"/>
                </View>

              </View>

              <View style={{
                  backgroundColor:"#FFF",
                  borderTopLeftRadius:40,
                  borderTopRightRadius:40,
                  height:1000,
                  paddingHorizontal:35
              }}>
                  <View style={{
                      flexDirection:"row",
                      paddingTop:20
                  }}>
                      <TouchableOpacity
                        onPress={this.onTabPressed}
                        style={{
                            borderBottomColor:this.state.popularSelected ? "#4969c2":"#FFF",
                            borderBottomWidth:4,
                            paddingVertical:6
                        }}
                      >
                          <Text style={{
                              fontFamily:"Bold",
                              color:this.state.popularSelected ? "#4969c2":"#9ca1a2"
                          }}>Самые популярные</Text>
                      </TouchableOpacity>


                      <TouchableOpacity
                        onPress={this.onTabPressed}
                        style={{
                            borderBottomColor:this.state.popularSelected ? "#FFF":"#4969c2",
                            borderBottomWidth:4,
                            paddingVertical:6,
                            marginLeft:30
                        }}
                      >
                          <Text style={{
                              fontFamily:"Bold",
                              color:this.state.popularSelected ? "#9ca1a2":"#4969c2"
                          }}>Последние</Text>
                      </TouchableOpacity>
                  </View>

                  <View style={{
                      flexDirection:"row"
                  }}>
                      <Posts
                        onPress={()=>this.props.navigation.navigate('Detail')}
                        name="Максим Бедак"
                        profile={require('../images/p1.jpg')}
                        photo={require('../images/item1.jpg')}
                      />


                      <View style={{
                          height:160,
                          backgroundColor:"#3c636c",
                          width:20,
                          marginLeft:20,
                          marginTop:120,
                          borderTopLeftRadius:20,
                          borderBottomLeftRadius:20
                      }}>

                      </View>
                                            

                  </View>



                  <View style={{
                      flexDirection:"row"
                  }}>
                     
                      <View style={{
                          height:160,
                          backgroundColor:"#3c636c",
                          width:20,
                          marginLeft:-40,
                          marginRight:20,
                          marginTop:120,
                          borderTopRightRadius:20,
                          borderBottomRightRadius:20
                      }}>

                      </View>

                      <Posts
                        onPress={()=>this.props.navigation.navigate('Detail')}
                        name="Ирина Биркина"
                        profile={require('../images/p2.jpg')}
                        photo={require('../images/item2.jpg')}
                      />

                  </View>

                  <View style={{
                      flexDirection:"row"
                  }}>
                      <Posts
                      
                        onPress={()=>this.props.navigation.navigate('Detail')}
                        name="Алексей Петров"
                        profile={require('../images/p1.jpg')}
                        photo={require('../images/item3.jpg')}
                      />

                      <View style={{
                          height:160,
                          backgroundColor:"#3c636c",
                          width:20,
                          marginLeft:20,
                          marginTop:120,
                          borderTopLeftRadius:20,
                          borderBottomLeftRadius:20
                      }}>

                      </View>

                  </View>
              </View>

          </ScrollView>
        )
    }
}