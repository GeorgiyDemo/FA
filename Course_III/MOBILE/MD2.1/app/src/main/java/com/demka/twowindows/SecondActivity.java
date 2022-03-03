package com.demka.twowindows;

import android.os.Bundle;
import android.widget.TextView;

public class SecondActivity extends MenuActivity {

    TextView textView;
    String value;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        Bundle extras = getIntent().getExtras();
        textView = findViewById(R.id.textView1);

        if (extras != null) {
            value = extras.getString("data");
            textView.setText(value);
        }

    }
}