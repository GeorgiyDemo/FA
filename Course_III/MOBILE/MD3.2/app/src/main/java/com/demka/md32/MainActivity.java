package com.demka.md32;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.material.floatingactionbutton.FloatingActionButton;

import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity {

    FloatingActionButton editButton;
    DBHelper dbHelper;

    RecyclerView myRecyclerView;
    MyAdapter myAdapter;

    ActivityResultLauncher<Intent> editActivity;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editButton = findViewById(R.id.editButton);
        myRecyclerView = findViewById(R.id.myRecyclerView);

        View.OnClickListener editButtonListener = this::editButtonClicked;

        editButton.setOnClickListener(editButtonListener);

        dbHelper = new DBHelper(this);
        myAdapter = new MyAdapter(this, dbHelper);
        myRecyclerView.setAdapter(myAdapter);
        myRecyclerView.setLayoutManager(new LinearLayoutManager(this));

        editActivity = registerForActivityResult(
                new ActivityResultContracts.StartActivityForResult(),
                result -> {
                    if (result.getResultCode() == AppCompatActivity.RESULT_OK) {
                        Intent data = result.getData();
                        if (data == null) {
                            return;
                        }
                        String content = data.getStringExtra("content");
                        String flag = data.getStringExtra("flag");

                        if (flag.equals("remove")) {
                            itemRemoved(content);
                        } else if (flag.equals("add")) {
                            itemAdded(content);
                        }
                    }
                }
        );
    }

    public void itemAdded(String data) {

        long index = dbHelper.addData(data);

        Map<String, String> newMap = new HashMap<>();
        newMap.put("id", String.valueOf(index));
        newMap.put("name", data);

        myAdapter.addItem(newMap);
        myAdapter.notifyItemInserted(myAdapter.dataList.size());
    }

    public void itemRemoved(String data) {

        dbHelper.deleteData(data);
        myAdapter.remove(data);
    }

    public void editButtonClicked(View v) {
        Intent intent = new Intent(this, EditItemActivity.class);
        editActivity.launch(intent);
    }
}