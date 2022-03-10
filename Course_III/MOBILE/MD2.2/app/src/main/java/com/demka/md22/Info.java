package com.demka.md22;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class Info extends AppCompatActivity {

    Button browserButton;
    Button phoneButton;
    Button mapButton;
    Button smsButton;
    EditText dataEditText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_info);

        browserButton = findViewById(R.id.browserButton);
        phoneButton = findViewById(R.id.phoneButton);
        mapButton = findViewById(R.id.mapButton);
        smsButton = findViewById(R.id.smsButton);
        dataEditText = findViewById(R.id.dataEditText);

        View.OnClickListener browserButtonListener = v -> browserButtonClicked();
        View.OnClickListener phoneButtonListener = v -> phoneButtonClicked();
        View.OnClickListener mapButtonListener = v -> mapButtonClicked();
        View.OnClickListener smsButtonListener = v -> smsButtonClicked();

        browserButton.setOnClickListener(browserButtonListener);
        phoneButton.setOnClickListener(phoneButtonListener);
        mapButton.setOnClickListener(mapButtonListener);
        smsButton.setOnClickListener(smsButtonListener);
    }


    public void browserButtonClicked(){

        String currentPath = "https://github.com/";
        if (!dataEditText.getText().toString().equals("")){
            currentPath = dataEditText.getText().toString();
        }
        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(currentPath));
        startActivity(intent);
    }

    public void phoneButtonClicked(){
        String currentPath = "79999999999";
        if (!dataEditText.getText().toString().equals("")){
            currentPath = dataEditText.getText().toString();
        }
        Intent intent = new Intent(Intent.ACTION_DIAL);
        intent.setData(Uri.parse("tel:"+currentPath));
        startActivity(intent);
    }

    public void mapButtonClicked(){
        Intent intent = new Intent(Intent.ACTION_VIEW);
        intent.setData(Uri.parse("geo:55.56,37.27"));
        startActivity(intent);
    }

    public void smsButtonClicked(){
        Intent intent = new Intent(Intent.ACTION_VIEW);
        intent.setData(Uri.parse("sms:79999999999"));
        intent.putExtra("sms_body","Тестовое сообщение");
        startActivity(intent);
    }
}
