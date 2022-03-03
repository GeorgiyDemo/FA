package com.demka.menu;

import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.CheckBox;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    // Элементы экрана
    TextView tv;
    CheckBox chb;


    /**
     * Called when the activity is first created.
     */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // находим элементы
        tv = findViewById(R.id.textView);
        chb = findViewById(R.id.chbExtMenu);
    }

    // создание меню
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // добавляем пункты меню
        menu.add(0, 1, 0, "add");
        menu.add(0, 2, 0, "edit");
        menu.add(0, 3, 3, "delete");
        menu.add(0, 4, 4, "more");
        menu.add(1, 5, 1, "copy");
        menu.add(1, 6, 2, "paste");
        menu.add(1, 7, 4, "exit");
        return super.onCreateOptionsMenu(menu);
    }

    // обновление меню
    @Override
    public boolean onPrepareOptionsMenu(Menu menu) {
        // пункты меню с ID группы = 1 видны, если в CheckBox стоит галка
        menu.setGroupVisible(1, chb.isChecked());
        return super.onPrepareOptionsMenu(menu);
    }


    // обработка нажатий
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {

        //Если это пункт exit, то завершаем приложение
        if (item.getItemId() == 7) {
            finish();
            return true;

        } else {

            StringBuilder sb = new StringBuilder();

            // Выведем в TextView информацию о нажатом пункте меню
            sb.append("Item Menu");
            sb.append("\r\n groupId: " + String.valueOf(item.getGroupId()));
            sb.append("\r\n itemId: " + String.valueOf(item.getItemId()));
            sb.append("\r\n order: " + String.valueOf(item.getOrder()));
            sb.append("\r\n title: " + item.getTitle());
            tv.setText(sb.toString());

            return super.onOptionsItemSelected(item);
        }
    }
}