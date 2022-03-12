package com.demka.md23;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class TODOCategoriesActivity extends AppCompatActivity {

    Button catButton1;
    Button catButton2;
    Button catButton3;
    Button catButton4;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_todocategories);

        catButton1 = findViewById(R.id.catButton1);
        catButton2 = findViewById(R.id.catButton2);
        catButton3 = findViewById(R.id.catButton3);
        catButton4 = findViewById(R.id.catButton4);

        View.OnClickListener categoryButtonListener = this::categoryButtonClicked;
        catButton1.setOnClickListener(categoryButtonListener);
        catButton2.setOnClickListener(categoryButtonListener);
        catButton3.setOnClickListener(categoryButtonListener);
        catButton4.setOnClickListener(categoryButtonListener);
    }


    public void categoryButtonClicked(View v) {
        Intent intent = new Intent(this, TODOItemsActivity.class);
        startActivity(intent);
    }


}