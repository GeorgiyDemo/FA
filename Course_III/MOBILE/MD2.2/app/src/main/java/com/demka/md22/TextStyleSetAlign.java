package com.demka.md22;

import android.content.Intent;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class TextStyleSetAlign extends AppCompatActivity {


    Button leftAlignButton;
    Button rightAlignButton;
    Button centerAlignButton;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_text_style_set_align);

        leftAlignButton = findViewById(R.id.leftAlignButton);
        rightAlignButton = findViewById(R.id.rightAlignButton);
        centerAlignButton = findViewById(R.id.centerAlignButton);

        View.OnClickListener allButtonListener = this::buttonClicked;

        leftAlignButton.setOnClickListener(allButtonListener);
        rightAlignButton.setOnClickListener(allButtonListener);
        centerAlignButton.setOnClickListener(allButtonListener);

    }

    public void buttonClicked(View v) {

        int currentGravity;
        switch (v.getId()) {
            case R.id.leftAlignButton:
                currentGravity = Gravity.LEFT;
                break;
            case R.id.rightAlignButton:
                currentGravity = Gravity.RIGHT;
                break;
            case R.id.centerAlignButton:
                currentGravity = Gravity.CENTER;
                break;
            default:
                throw new IllegalStateException("Unexpected value: " + v.getId());
        }

        Intent intent = new Intent();
        intent.putExtra("gravity", String.valueOf(currentGravity));
        setResult(RESULT_OK, intent);
        finish();
    }
}