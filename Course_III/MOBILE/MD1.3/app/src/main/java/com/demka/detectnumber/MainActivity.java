package com.demka.detectnumber;

import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.view.inputmethod.InputMethodManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Button mainButton;
    Button resetButton;
    TextView mainTextView;
    TextView subTextView;
    EditText editTextNumber;
    RadioButton radioButtonEasy;
    RadioButton radioButtonMiddle;
    RadioButton radioButtonHard;

    int randomNumber;
    int minRangeNumber;
    int maxRangeNumber;
    boolean isInGame = false;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mainButton = findViewById(R.id.mainButton);
        resetButton = findViewById(R.id.resetButton);
        mainTextView = findViewById(R.id.mainTextView);
        editTextNumber = findViewById(R.id.editTextNumber);
        radioButtonEasy = findViewById(R.id.radioButtonEasy);
        radioButtonMiddle = findViewById(R.id.radioButtonMiddle);
        radioButtonHard = findViewById(R.id.radioButtonHard);
        subTextView = findViewById(R.id.subTextView);

        resetButton.setVisibility(View.INVISIBLE);

        View.OnClickListener mainButtonListener = v -> mainButtonClick();
        View.OnClickListener radioButtonListener = v -> startGame();

        radioButtonEasy.setOnClickListener(radioButtonListener);
        radioButtonMiddle.setOnClickListener(radioButtonListener);
        radioButtonHard.setOnClickListener(radioButtonListener);
        resetButton.setOnClickListener(radioButtonListener);

        mainButton.setOnClickListener(mainButtonListener);

    }

    /**
     * Метод нажатия на основную кнопку
     */
    private int mainButtonClick() {
        //Если игра еще не началась
        if (!isInGame) {
            startGame();
            return 0;
        }

        //Если игра уже идет и если не ввели число
        if (editTextNumber.getText().toString().equals("")) {
            Toast toast = Toast.makeText(getApplicationContext(), "Необходимо ввести число!", Toast.LENGTH_SHORT);
            toast.show();
            return 0;
        }

        int currentNumber = Integer.parseInt(editTextNumber.getText().toString());
        if ((currentNumber > maxRangeNumber) || (currentNumber < minRangeNumber)) {
            String currentErrorStr = String.format("Число %s не принадлежит диапазону %s - %s", currentNumber, minRangeNumber, maxRangeNumber);
            Toast toast = Toast.makeText(getApplicationContext(), currentErrorStr, Toast.LENGTH_SHORT);
            toast.show();
            return 0;
        }

        if (currentNumber < randomNumber) {
            //Недолет
            subTextView.setText(getResources().getString(R.string.behind));
            return 0;
        }

        if (currentNumber > randomNumber) {
            //Пререлет
            subTextView.setText(getResources().getString(R.string.ahead));
            return 0;
        }

        //Если они совпадают
        subTextView.setText(getResources().getString(R.string.hit));
        resetButton.setVisibility(View.VISIBLE);
        //Скрываем клавиатуру
        View view = this.getCurrentFocus();
        if (view != null) {
            InputMethodManager imm = (InputMethodManager) getSystemService(Context.INPUT_METHOD_SERVICE);
            imm.hideSoftInputFromWindow(view.getWindowToken(), 0);
        }
        return 0;
    }

    /**
     * Возвращает максимальное число для диапазона в зависимости от выранного уровня сложности
     *
     * @return максимальное значение для выбранного radioButton
     */
    private int maxRangeDetector() {
        if (radioButtonHard.isChecked()) {
            return 500;
        }
        if (radioButtonMiddle.isChecked()) {
            return 250;
        }
        return 100;
    }

    /**
     * Метод для начала игры
     */
    private void startGame() {

        resetButton.setVisibility(View.INVISIBLE);
        minRangeNumber = 0;
        maxRangeNumber = maxRangeDetector();
        randomNumber = (int) ((Math.random() * (maxRangeNumber)) + minRangeNumber);
        String currentRangeStr = String.format("Попробуйте угадать число от %s до %s", minRangeNumber, maxRangeNumber);
        mainTextView.setText(currentRangeStr);
        editTextNumber.setText("");
        subTextView.setText("");
        isInGame = true;
    }
}