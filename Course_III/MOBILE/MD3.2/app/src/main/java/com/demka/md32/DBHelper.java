package com.demka.md32;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.util.Log;

import java.util.ArrayList;
import java.util.List;

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

    public void addData(String data) {

        ContentValues cv = new ContentValues();
        SQLiteDatabase db = getWritableDatabase();

        Log.i("LOG_TAG", data);
        cv.put("name", data);
        db.insert("mytable", null, cv);
    }

    public boolean deleteData(String data) {
        ContentValues cv = new ContentValues();
        SQLiteDatabase db = getWritableDatabase();
        String whereClause = String.format("name='%s'", data);
        int result = db.delete("mytable", whereClause, null);
        return result == 1;
    }

    public List<String> getData() {
        List<String> resultList = new ArrayList<>();
        SQLiteDatabase db = getWritableDatabase();

        Cursor c = db.query("mytable", null, null, null, null, null, null);
        if (c.moveToFirst()) {
            int idColIndex = c.getColumnIndex("id");
            int nameColIndex = c.getColumnIndex("name");
            do {

                resultList.add(c.getString(nameColIndex));
                Log.d("LOG_TAG", "ID = " + c.getInt(idColIndex) + ", name = " + c.getString(nameColIndex));
            } while (c.moveToNext());

        } else
            Log.d("LOG_TAG", "0 rows");
        c.close();

        return resultList;
    }
}
