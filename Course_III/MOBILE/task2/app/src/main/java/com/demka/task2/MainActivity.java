package com.demka.task2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    Button number0;
    Button number1;
    Button number2;
    Button number3;
    Button number4;
    Button number5;
    Button number6;
    Button number7;
    Button number8;
    Button number9;

    Button buttonplus;
    Button buttonminus;

    TextView inputtext1;
    TextView inputtext2;
    TextView inputtext3;

    TextView currentTextView;
    Boolean isSecondValue;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        isSecondValue = false;

        number0 = findViewById(R.id.number0);
        number1 = findViewById(R.id.number1);
        number2 = findViewById(R.id.number2);
        number3 = findViewById(R.id.number3);
        number4 = findViewById(R.id.number4);
        number5 = findViewById(R.id.number5);
        number6 = findViewById(R.id.number6);
        number7 = findViewById(R.id.number7);
        number8 = findViewById(R.id.number8);
        number9 = findViewById(R.id.number9);

        buttonplus = findViewById(R.id.buttonplus);
        buttonminus = findViewById(R.id.buttonminus);

        inputtext1 = findViewById(R.id.inputtext1);
        inputtext2 = findViewById(R.id.inputtext2);
        inputtext3 = findViewById(R.id.inputtext3);


        number0.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {

                if (isSecondValue){
                    inputtext3.setText(inputtext3.getText()+"0");
                }
                else{
                    inputtext1.setText(inputtext1.getText()+"0");
                }

            }
        });

        number1.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {

                if (isSecondValue){
                    inputtext3.setText(inputtext3.getText()+"1");
                }
                else{
                    inputtext1.setText(inputtext1.getText()+"1");
                }
            }
        });

        number2.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {

                if (isSecondValue){
                    inputtext3.setText(inputtext3.getText()+"2");
                }
                else{
                    inputtext1.setText(inputtext1.getText()+"2");
                }
            }
        });

        number3.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {

                if (isSecondValue){
                    inputtext3.setText(inputtext3.getText()+"3");
                }
                else{
                    inputtext1.setText(inputtext1.getText()+"3");
                }
            }
        });

        number4.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {

                if (isSecondValue){
                    inputtext3.setText(inputtext3.getText()+"4");
                }
                else{
                    inputtext1.setText(inputtext1.getText()+"4");
                }
            }
        });

        number5.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {

                if (isSecondValue){
                    inputtext3.setText(inputtext3.getText()+"5");
                }
                else{
                    inputtext1.setText(inputtext1.getText()+"5");
                }
            }
        });

        number6.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {

                if (isSecondValue){
                    inputtext3.setText(inputtext3.getText()+"6");
                }
                else{
                    inputtext1.setText(inputtext1.getText()+"6");
                }
            }
        });

        number7.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {

                if (isSecondValue){
                    inputtext3.setText(inputtext3.getText()+"7");
                }
                else{
                    inputtext1.setText(inputtext1.getText()+"7");
                }
            }
        });

        number8.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {

                if (isSecondValue){
                    inputtext3.setText(inputtext3.getText()+"8");
                }
                else{
                    inputtext1.setText(inputtext1.getText()+"8");
                }
            }
        });

        number9.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {

                if (isSecondValue){
                    inputtext3.setText(inputtext3.getText()+"9");
                }
                else{
                    inputtext1.setText(inputtext1.getText()+"9");
                }
            }
        });



        buttonplus.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                isSecondValue = true;
                inputtext2.setText("+");
            }
        });

        buttonminus.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                isSecondValue = true;
                inputtext2.setText("-");
            }
        });








    }
}