package com.demka.md23;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;

public class TODOItemsActivity extends AppCompatActivity {

    EditText mainEditText;
    ListView mainListView;
    Button mainButton;
    ArrayAdapter<String> mArrayAdapter;
    ArrayList<String> mNameList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_todoitems);

        mainListView = findViewById(R.id.main_listview);
        mainButton = findViewById(R.id.main_button);
        mainEditText = findViewById(R.id.main_edittext);

        View.OnClickListener mainButtonListener = this::mainButtonClicked;
        mainButton.setOnClickListener(mainButtonListener);
        mArrayAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, mNameList);
        mainListView.setAdapter(mArrayAdapter);
        mainListView.setOnItemClickListener(new AdapterView.OnItemClickListener() {

            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                String text = mNameList.get(position);
                mNameList.remove(position);
                mArrayAdapter.notifyDataSetChanged();
                Toast.makeText(getApplicationContext(), String.format("%s выполнено", text), Toast.LENGTH_LONG).show();
            }
        });
    }

    public void mainButtonClicked(View v) {
        String newItemStr = mainEditText.getText().toString();
        //Если ничего не написали
        if (newItemStr.equals("")) {
            Toast.makeText(getApplicationContext(), "Нельзя добавить пустой элемент в список", Toast.LENGTH_LONG).show();
            return;
        }

        //Проверяем, чтоб элемент все еще не был в списке
        for (String item : mNameList) {
            if (item.equals(newItemStr)) {
                String errorStr = String.format("Элемент %s уже есть в этом списке", newItemStr);
                Toast.makeText(getApplicationContext(), errorStr, Toast.LENGTH_LONG).show();
                return;
            }
        }

        mNameList.add(newItemStr);
        mArrayAdapter.notifyDataSetChanged();
    }
}