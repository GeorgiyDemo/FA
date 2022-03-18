package com.demka.md32;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    Button btnAdd;
    Button btnDelete;
    Button btnRead;
    EditText etName;
    DBHelper dbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnAdd = findViewById(R.id.btnAdd);
        btnDelete = findViewById(R.id.btnDelete);
        btnRead = findViewById(R.id.btnRead);
        etName = findViewById(R.id.etName);

        View.OnClickListener addButtonListener = this::addButtonClicked;
        View.OnClickListener deleteButtonListener = this::deleteButtonClicked;
        View.OnClickListener readButtonListener = this::readButtonClicked;

        btnAdd.setOnClickListener(addButtonListener);
        btnDelete.setOnClickListener(deleteButtonListener);
        btnRead.setOnClickListener(readButtonListener);

        dbHelper = new DBHelper(this);

    }

    public void addButtonClicked(View v) {
        String data = etName.getText().toString();
        dbHelper.addData(data);
    }

    public void deleteButtonClicked(View v) {
        String data = etName.getText().toString();
        dbHelper.deleteData(data);

    }

    public void readButtonClicked(View v) {
        dbHelper.getData();
    }
}