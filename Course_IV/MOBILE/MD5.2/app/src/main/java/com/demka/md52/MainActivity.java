package com.demka.md52;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

public class MainActivity extends AppCompatActivity {

    Button startServiceButton;
    Button stopServiceButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        startServiceButton = findViewById(R.id.startServiceButton);
        stopServiceButton = findViewById(R.id.stopServiceButton);

        View.OnClickListener startButtonListener = this::startServiceButtonClicked;
        startServiceButton.setOnClickListener(startButtonListener);

        View.OnClickListener stopButtonListener = this::stopServiceButtonClicked;
        stopServiceButton.setOnClickListener(stopButtonListener);

    }

    public void startServiceButtonClicked(View v) {
        Log.i("CHECK", "startServiceButtonClicked");
        Intent serviceIntent = new Intent(this, ForegroundService.class);
        serviceIntent.putExtra("inputExtra", "Foreground Service Example in Android");
        ContextCompat.startForegroundService(this, serviceIntent);


    }

    public void stopServiceButtonClicked(View v) {
        Log.i("CHECK", "stopServiceButtonClicked");
        Intent serviceIntent = new Intent(this, ForegroundService.class);
        stopService(serviceIntent);
    }
}