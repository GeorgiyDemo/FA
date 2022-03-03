package com.demka.twowindows;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class FirstActivity extends MenuActivity {


    final String TAG = "States";
    Button btnActTwo;
    EditText editText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btnActTwo = findViewById(R.id.btnActTwo);
        editText = findViewById(R.id.editText);

        View.OnClickListener btnListener = this::onClick;
        btnActTwo.setOnClickListener(btnListener);

    }

    public void onClick(View v) {
        if (editText.getText().toString().equals("")) {
            Toast.makeText(getApplicationContext(), "Введите текст", Toast.LENGTH_LONG).show();
        } else {
            Intent intent = new Intent(this, SecondActivity.class);
            intent.putExtra("data", editText.getText().toString());
            startActivity(intent);
            Log.d(TAG, "MainActivity: onCreate()");
        }
    }

    @Override
    protected void onStart() {
        super.onStart();
        Log.d(TAG, "MainActivity: onStart()");
    }

    @Override
    protected void onResume() {
        super.onResume();
        Log.d(TAG, "MainActivity: onResume()");
    }

    @Override
    protected void onPause() {
        super.onPause();
        Log.d(TAG, "MainActivity: onPause()");
    }

    @Override
    protected void onStop() {
        super.onStop();
        Log.d(TAG, "MainActivity: onStop()");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.d(TAG, "MainActivity: onDestroy()");
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Log.d(TAG, "MainActivity: onRestart()");
    }


}