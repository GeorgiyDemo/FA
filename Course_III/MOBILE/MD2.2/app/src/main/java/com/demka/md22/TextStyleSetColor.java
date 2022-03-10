package com.demka.md22;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class TextStyleSetColor extends AppCompatActivity {

    Button redColorButton;
    Button greenColorButton;
    Button blueColorButton;
    Button pinkColorButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_text_style_set_color);

        redColorButton = findViewById(R.id.redColorButton);
        greenColorButton = findViewById(R.id.greenColorButton);
        blueColorButton = findViewById(R.id.blueColorButton);
        pinkColorButton = findViewById(R.id.pinkColorButton);

        View.OnClickListener allButtonListener = this::buttonClicked;
        redColorButton.setOnClickListener(allButtonListener);
        greenColorButton.setOnClickListener(allButtonListener);
        blueColorButton.setOnClickListener(allButtonListener);
        pinkColorButton.setOnClickListener(allButtonListener);
    }


    public void buttonClicked(View v) {


        int currentColor;

        switch (v.getId()) {
            case R.id.redColorButton:
                currentColor = Color.RED;
                break;
            case R.id.greenColorButton:
                currentColor = Color.GREEN;
                break;
            case R.id.blueColorButton:
                currentColor = Color.BLUE;
                break;
            case R.id.pinkColorButton:
                currentColor = Color.MAGENTA;
                break;
            default:
                throw new IllegalStateException("Unexpected value: " + v.getId());
        }

        Intent intent = new Intent();
        intent.putExtra("color", String.valueOf(currentColor));
        setResult(RESULT_OK, intent);
        finish();
    }

}