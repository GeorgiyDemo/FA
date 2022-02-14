package com.demka.task2;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.math.BigDecimal;
import java.math.RoundingMode;

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

    Button additionButton;
    Button subtractionButton;
    Button multiplicationButton;
    Button divisionButton;
    Button resultButton;
    Button cancelButton;

    TextView textViewFirstNumber;
    TextView textViewOp;
    TextView textViewSecondNumber;
    TextView textViewEqualOp;
    TextView textViewResult;

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

        additionButton = findViewById(R.id.additionButton);
        subtractionButton = findViewById(R.id.subtractionButton);
        multiplicationButton = findViewById(R.id.multiplicationButton);
        divisionButton = findViewById(R.id.divisionButton);
        resultButton = findViewById(R.id.resultButton);
        cancelButton = findViewById(R.id.cancelButton);

        textViewFirstNumber = findViewById(R.id.textViewFirstNumber);
        textViewOp = findViewById(R.id.textViewOp);
        textViewSecondNumber = findViewById(R.id.textViewSecondNumber);
        textViewEqualOp = findViewById(R.id.textViewEqualOp);
        textViewResult = findViewById(R.id.textViewResult);

        textViewEqualOp.setVisibility(View.INVISIBLE);

        number0.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textSender(isSecondValue, "0");
            }
        });

        number1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textSender(isSecondValue, "1");
            }
        });

        number2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textSender(isSecondValue, "2");
            }
        });

        number3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textSender(isSecondValue, "3");
            }
        });

        number4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textSender(isSecondValue, "4");
            }
        });

        number5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textSender(isSecondValue, "5");
            }
        });

        number6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textSender(isSecondValue, "6");
            }
        });

        number7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textSender(isSecondValue, "7");
            }
        });

        number8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textSender(isSecondValue, "8");
            }
        });

        number9.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                textSender(isSecondValue, "9");
            }
        });


        additionButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                isSecondValue = true;
                textViewOp.setText("+");
            }
        });

        subtractionButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                isSecondValue = true;
                textViewOp.setText("-");
            }
        });

        multiplicationButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                isSecondValue = true;
                textViewOp.setText("*");
            }
        });

        divisionButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                isSecondValue = true;
                textViewOp.setText("/");
            }
        });

        resultButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                resultButtonClicked(textViewOp.getText().toString());
            }
        });

        cancelButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                cancelButtonClicked();
            }
        });

    }


    /**
     * Метод для самой логики вычисления
     *
     * @param currentOp - текст с TextView с текущей операцией
     */
    private void resultButtonClicked(String currentOp) {

        Double result = 0.0;
        Double firstValue = Double.parseDouble(textViewFirstNumber.getText().toString());
        Double secondValue = Double.parseDouble(textViewSecondNumber.getText().toString());

        textViewEqualOp.setVisibility(View.VISIBLE);
        try {
            switch (currentOp) {
                case ("+"):
                    result = firstValue + secondValue;
                    break;
                case ("-"):
                    result = firstValue - secondValue;
                    break;
                case ("*"):
                    result = firstValue * secondValue;
                    break;
                case ("/"):
                    result = firstValue / secondValue;
                    break;
            }
            textViewResult.setText(Double.toString(round(result, 12)));
        } catch (Exception e) {
            textViewResult.setText(R.string.error);
        }

    }

    /**
     * Нажатие на кнопку сброса вычислений
     */
    private void cancelButtonClicked() {
        isSecondValue = false;
        textViewOp.setText("");
        textViewFirstNumber.setText("");
        textViewSecondNumber.setText("");
        textViewResult.setText("");
        textViewEqualOp.setVisibility(View.INVISIBLE);

    }

    /**
     * Метод для добавления данных в textView в числами, над которыми производим вычисления
     *
     * @param isSecondValue - ввод первого или 2 значения
     * @param value         - само значение, которое вводим
     */

    private void textSender(Boolean isSecondValue, String value) {
        if (isSecondValue) {
            textViewSecondNumber.setText(textViewSecondNumber.getText() + value);
        } else {
            textViewFirstNumber.setText(textViewFirstNumber.getText() + value);
        }
    }


    /**
     * Округление данных
     *
     * @param value  - значение для округления
     * @param places - на сколько знаков округляем
     * @return - округленное значение
     */
    private double round(double value, int places) {
        if (places < 0) throw new IllegalArgumentException();

        BigDecimal bd = BigDecimal.valueOf(value);
        bd = bd.setScale(places, RoundingMode.HALF_UP);
        return bd.doubleValue();
    }
}