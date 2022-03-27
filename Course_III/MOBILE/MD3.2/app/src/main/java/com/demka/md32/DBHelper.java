package com.demka.md32;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DBHelper extends SQLiteOpenHelper {

    public DBHelper(Context context) {
        super(context, "MyDB", null, 1);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {

    }

    public long addData(String data) {

        ContentValues cv = new ContentValues();
        SQLiteDatabase db = getWritableDatabase();

        cv.put("name", data);
        long index = db.insert("mytable", null, cv);
        return index;
    }

    public boolean deleteData(String data) {
        SQLiteDatabase db = getWritableDatabase();
        String whereClause = String.format("name='%s'", data);
        int result = db.delete("mytable", whereClause, null);
        return result == 1;
    }

    public List<Map<String, String>> getData() {
        List<Map<String, String>> resultList = new ArrayList<>();
        SQLiteDatabase db = getWritableDatabase();

        Cursor c = db.query("mytable", null, null, null, null, null, null);

        if (c.moveToFirst()) {
            int idColIndex = c.getColumnIndex("id");
            int nameColIndex = c.getColumnIndex("name");
            do {
                Map<String, String> bufMap = new HashMap<>();
                bufMap.put("id", c.getString(idColIndex));
                bufMap.put("name", c.getString(nameColIndex));
                resultList.add(bufMap);
            } while (c.moveToNext());

        }

        c.close();
        return resultList;
    }
}
