package com.demka.md22;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;

public class TextStyleEditor extends AppCompatActivity {

    Button changeColorButton;
    Button changeAlignButton;
    TextView mainTextView;

    ActivityResultLauncher<Intent> colorResultActivity;
    ActivityResultLauncher<Intent> alignResultActivity;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_text_style_editor);

        changeColorButton = findViewById(R.id.changeColorButton);
        changeAlignButton = findViewById(R.id.changeAlignButton);
        mainTextView = findViewById(R.id.mainTextView);

        View.OnClickListener changeColorButtonListener = v -> colorButtonClicked();
        View.OnClickListener changeAlignButtonListener = v -> alignButtonClicked();

        changeColorButton.setOnClickListener(changeColorButtonListener);
        changeAlignButton.setOnClickListener(changeAlignButtonListener);

        colorResultActivity = registerForActivityResult(
                new ActivityResultContracts.StartActivityForResult(),
                result -> {
                    if (result.getResultCode() == AppCompatActivity.RESULT_OK) {
                        Intent data = result.getData();
                        if (data == null) {
                            return;
                        }
                        String color = data.getStringExtra("color");
                        mainTextView.setTextColor(Integer.parseInt(color));
                    }
                }
        );

        alignResultActivity = registerForActivityResult(
                new ActivityResultContracts.StartActivityForResult(),
                result -> {
                    if (result.getResultCode() == AppCompatActivity.RESULT_OK) {
                        Intent data = result.getData();
                        if (data == null) {
                            return;
                        }
                        String gravity = data.getStringExtra("gravity");
                        mainTextView.setGravity(Integer.parseInt(gravity));
                    }
                }
        );
    }

    public void colorButtonClicked() {
        Intent intent = new Intent(this, TextStyleSetColor.class);
        colorResultActivity.launch(intent);
    }

    public void alignButtonClicked() {
        Intent intent = new Intent(this, TextStyleSetAlign.class);
        alignResultActivity.launch(intent);
    }


}