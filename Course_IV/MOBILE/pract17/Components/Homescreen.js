// HomeScreen.js

import React from 'react';
import { ScrollView, StatusBar } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import styled from 'styled-components/native';

const Container = styled.View`
  flex: 1;
  margin-top: 36px;
`;

const Section = styled.View`
  margin-bottom: 32px;
  border-radius: 8px;
  elevation: 5;
`;

const Circle = styled.View`
  width: 200px;
  height: 200px;
  border-radius: 100px;
  align-items: center;
  background-color: white;
  justify-content: center;
  border: 8px solid #57b7d0;
`;

const CircleText = styled.Text`
  font-size: 36px;
  font-weight: bold;
  color: #333;
`;

const SectionTitle = styled.Text`
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 8px;
  padding: 8px 16px;
  background-color: #333;
  color: #fff;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
`;

const CardContainer = styled.View`
  flex-direction: row;
  flex-wrap: wrap;
`;

const Card = styled.View`
  width: 50%;
  aspect-ratio: 1;
  padding: 8px;
`;

const CardImage = styled.Image`
  width: 100%;
  height: 100%;
  border-radius: 8px;
`;

const CardTitle = styled.Text`
  font-size: 16px;
  margin: 8px;
`;

const ActivityCard = styled.View`
  aspect-ratio: 1;
  padding: 8px;
  background-color: #fff;
  border-radius: 8px;
  elevation: 5;
`;

const ActivityImage = styled.Image`
  width: 100%;
  height: 200px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
`;

const ActivityTitle = styled.Text`
  font-size: 20px;
  font-weight: bold;
  margin: 8px;
`;

const ActivityDescription = styled.Text`
  font-size: 16px;
  margin: 8px;
`;


const HomeScreen = () => {
  return (
    <ScrollView>
           <StatusBar backgroundColor={"#333"} />    
      <Container>
        
        {/* Первая секция */}
        <LinearGradient
          colors={['#a553ac', '#222337']}
          start={{ x: 0, y: 0 }}
          end={{x: 1, y: 1 }}
        >
          <Section>
            <Circle>
              <CircleText>75%</CircleText>
            </Circle>
          </Section>


        {/* Вторая секция */}

          <Section>
            <SectionTitle>Discover</SectionTitle>
            <CardContainer>
              <Card>
                <CardImage source={require('../assets/image.png')} />
                <CardTitle>Daily workout</CardTitle>
              </Card>
              <Card>
                <CardImage source={require('../assets/image.png')} />
                <CardTitle>Programs</CardTitle>
              </Card>
              <Card>
                <CardImage source={require('../assets/image.png')} />
                <CardTitle>Tech. Guides</CardTitle>
              </Card>
              <Card>
                <CardImage source={require('../assets/image.png')} />
                <CardTitle>Training spots</CardTitle>
              </Card>
            </CardContainer>
          </Section>


        {/* Третья секция */}

          <Section>
          <SectionTitle>Recent activity</SectionTitle>
          <ActivityCard>
            <ActivityImage source={require('../assets/image.png')} />
            <ActivityTitle>Workout session</ActivityTitle>
            <ActivityDescription>
              You completed a 30-minute workout session. Keep up the good work!
            </ActivityDescription>
          </ActivityCard>
          </Section>
        </LinearGradient>
      </Container>
    </ScrollView>
  );
};

export default HomeScreen;