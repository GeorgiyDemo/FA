package com.demka.md51;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private Button startButton, stopButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        startButton = findViewById(R.id.startServiceButton);
        stopButton = findViewById(R.id.stopServiceButton);


        startButton.setOnClickListener(this);
        stopButton.setOnClickListener(this);
    }

    public void onClick(View view) {

        if (view == startButton) {

            startService(new Intent(this, NewService.class));
        } else if (view == stopButton) {

            stopService(new Intent(this, NewService.class));
        }
    }
}