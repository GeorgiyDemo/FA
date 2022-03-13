package com.demka.md31;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Button btnSave;
    Button btnLoad;
    EditText etName;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnSave = findViewById(R.id.btnSave);
        btnLoad = findViewById(R.id.btnLoad);
        etName = findViewById(R.id.etName);

        View.OnClickListener btnSaveListener = this::btnSaveClicked;
        View.OnClickListener btnLoadListener = this::btnLoadClicked;

        btnSave.setOnClickListener(btnSaveListener);
        btnLoad.setOnClickListener(btnLoadListener);

        etName.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {
                dumpData();
            }
        });
        loadData();


    }

    public void btnSaveClicked(View v) {
        dumpData();
    }

    public void btnLoadClicked(View v) {
        loadData();
    }

    public void loadData() {
        SharedPreferences pref = getPreferences(MODE_PRIVATE);
        String name = pref.getString("name", "");
        etName.setText(name);
    }

    public void dumpData() {
        SharedPreferences pref = getPreferences(MODE_PRIVATE);
        SharedPreferences.Editor ed = pref.edit();
        String name = etName.getText().toString();
        ed.putString("name", name);
        ed.apply();
    }
}