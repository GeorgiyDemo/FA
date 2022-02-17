package com.demka.clicker;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    TextView mainText;
    Button incButton;
    Button decButton;
    Button resetButton;
    ImageView imageView;

    private int score = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        incButton = findViewById(R.id.incButton);
        decButton = findViewById(R.id.decButton);
        resetButton = findViewById(R.id.resetButton);

        mainText = findViewById(R.id.mainText);
        imageView = findViewById(R.id.imageView3);

        View.OnClickListener incListener = v -> {
            score++;
            String itemPlural = getResources().getQuantityString(R.plurals.plurals, score);
            String s = "Кнопка нажата " + score + " " + itemPlural;
            mainText.setText(s.toCharArray(), 0, s.length());
        };

        View.OnClickListener decListener = v -> {
            score--;
            String itemPlural = getResources().getQuantityString(R.plurals.plurals, score);
            String s = "Кнопка нажата " + score + " " + itemPlural;
            mainText.setText(s.toCharArray(), 0, s.length());
        };

        View.OnClickListener resetListener = v -> {
            score = 0;
            String s = "Кнопка нажата 0 раз";
            mainText.setText(s.toCharArray(), 0, s.length());
        };

        incButton.setOnClickListener(incListener);
        imageView.setOnClickListener(incListener);
        decButton.setOnClickListener(decListener);
        resetButton.setOnClickListener(resetListener);
    }
}