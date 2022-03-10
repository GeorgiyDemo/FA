package com.demka.md22;

import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.text.SimpleDateFormat;
import java.util.Date;

public class ActivityTime extends AppCompatActivity {

    TextView tvTime;
    TextView textView;
    String time;
    SimpleDateFormat sdf;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_time);

        sdf = new SimpleDateFormat("HH:mm:ss");
        time = sdf.format(new Date(System.currentTimeMillis()));
        tvTime = findViewById(R.id.tvDate);
        textView = findViewById(R.id.tvView);
        tvTime.setText(time);

        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            String value = extras.getString("lname");
            textView.setText(value);
        }


    }

}