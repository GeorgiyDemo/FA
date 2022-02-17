package com.demka.detectnumber;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    Button mainButton;
    TextView mainTextView;
    EditText editTextNumber;
    RadioButton radioButtonEasy;
    RadioButton radioButtonMiddle;
    RadioButton radioButtonHard;

    boolean isInGame = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mainButton = findViewById(R.id.mainButton);
        mainTextView = findViewById(R.id.mainTextView);
        editTextNumber = findViewById(R.id.editTextNumber);
        radioButtonEasy = findViewById(R.id.radioButtonEasy);
        radioButtonMiddle = findViewById(R.id.radioButtonMiddle);
        radioButtonHard = findViewById(R.id.radioButtonHard);

        View.OnClickListener mainButtonListener = v -> mainButtonClick();

        mainButton.setOnClickListener(mainButtonListener);

    }

    /**
     * Метод нажатия на основную кнопку
     */
    private void mainButtonClick(){

    }

    private void gameProcessing(){
        if (isInGame){

        }

    }

    /**
     * Событийный метод для изменения уровня игры
     * Чем больше уровень - тем больше диапазон чисел
     */
    private void gameLevelChanger(){

    }
}