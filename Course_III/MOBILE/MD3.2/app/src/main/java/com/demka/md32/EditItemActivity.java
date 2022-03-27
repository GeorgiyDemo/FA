package com.demka.md32;

import android.content.Intent;
import android.database.DatabaseUtils;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class EditItemActivity extends AppCompatActivity {

    Button addButton;
    Button removeButton;
    EditText itemName;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_item);

        itemName = findViewById(R.id.itemName);
        addButton = findViewById(R.id.addButton);
        removeButton = findViewById(R.id.removeButton);

        View.OnClickListener addButtonListener = this::addButtonClicked;
        View.OnClickListener removeButtonListener = this::removeButtonClicked;

        addButton.setOnClickListener(addButtonListener);
        removeButton.setOnClickListener(removeButtonListener);
    }

    public void addButtonClicked(View v) {

        if (getUserInputText().equals("")) {
            Toast.makeText(getApplicationContext(), "Необходимо заполнить текстовое поле", Toast.LENGTH_SHORT).show();
            return;
        }

        Intent intent = new Intent();
        intent.putExtra("flag", "add");
        intent.putExtra("content", getUserInputText());
        setResult(RESULT_OK, intent);
        finish();
    }

    public void removeButtonClicked(View v) {

        if (getUserInputText().equals("")) {
            Toast.makeText(getApplicationContext(), "Необходимо заполнить текстовое поле", Toast.LENGTH_SHORT).show();
            return;
        }

        Intent intent = new Intent();
        intent.putExtra("flag", "remove");
        intent.putExtra("content", getUserInputText());
        setResult(RESULT_OK, intent);
        finish();
    }

    private String getUserInputText(){
        return itemName.getText().toString().replaceAll("'","");
    }
}