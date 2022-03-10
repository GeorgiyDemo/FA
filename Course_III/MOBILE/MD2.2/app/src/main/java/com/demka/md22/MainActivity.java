package com.demka.md22;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Button btnDate;
    Button btnTime;
    Button getValueButton;
    Button textStyleEditorButton;
    EditText etLName;
    TextView tvName;

    ActivityResultLauncher<Intent> startActivityForResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnDate = findViewById(R.id.btnDate);
        btnTime = findViewById(R.id.btnTime);
        etLName = findViewById(R.id.etLName);
        tvName = findViewById(R.id.tvName);
        textStyleEditorButton = findViewById(R.id.textStyleEditorButton);
        getValueButton = findViewById(R.id.getValueButton);

        View.OnClickListener timeListener = v -> btnTimeClicked();
        View.OnClickListener dateListener = v -> btnDateClicked();
        View.OnClickListener getValueButtonListener = v -> getValueButtonClicked();
        View.OnClickListener textStyleEditorListener = v -> textStyleEditorButtonClicked();

        textStyleEditorButton.setOnClickListener(textStyleEditorListener);
        getValueButton.setOnClickListener(getValueButtonListener);
        btnTime.setOnClickListener(timeListener);
        btnDate.setOnClickListener(dateListener);

        startActivityForResult = registerForActivityResult(
                new ActivityResultContracts.StartActivityForResult(),
                result -> {
                    if (result.getResultCode() == AppCompatActivity.RESULT_OK) {
                        Intent data = result.getData();
                        if (data == null) {
                            return;
                        }
                        String name = data.getStringExtra("name");
                        tvName.setText("Your name is " + name);
                    }
                }
        );

    }

    public void textStyleEditorButtonClicked(){
        Intent intent = new Intent(this, TextStyleEditor.class);
        startActivity(intent);
    }

    public void btnTimeClicked() {
        Intent intent = new Intent("com.demka.md22.intent.action.showtime");
        intent.putExtra("lname", etLName.getText().toString());
        startActivity(intent);
    }

    public void btnDateClicked() {
        Intent intent = new Intent("com.demka.md22.intent.action.showdate");
        intent.putExtra("lname", etLName.getText().toString());
        startActivity(intent);
    }

    public void getValueButtonClicked() {
        Intent intent = new Intent(this, SetResultActivity.class);
        startActivityForResult.launch(intent);
    }


}