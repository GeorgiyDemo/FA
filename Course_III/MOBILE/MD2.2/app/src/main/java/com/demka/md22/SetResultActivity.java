package com.demka.md22;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class SetResultActivity extends AppCompatActivity {

    TextView etName;
    TextView textView1;
    Button btnOK;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_set_result);

        etName = findViewById(R.id.etName);
        textView1 = findViewById(R.id.textView1);
        btnOK = findViewById(R.id.btnOK);

        View.OnClickListener mainListener = this::btnOkClicked;
        btnOK.setOnClickListener(mainListener);

    }

    public void btnOkClicked(View v) {
        Intent intent = new Intent();
        intent.putExtra("name", etName.getText().toString());
        setResult(RESULT_OK, intent);
        finish();
    }
}