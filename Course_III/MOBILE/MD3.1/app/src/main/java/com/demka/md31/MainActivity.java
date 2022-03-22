package com.demka.md31;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.drawable.BitmapDrawable;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Base64;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

import java.io.ByteArrayOutputStream;

public class MainActivity extends AppCompatActivity {

    Button btnSave;
    Button btnLoad;
    EditText etName;
    Button photoButton;
    ImageView mainImageView;
    private static final int CAMERA_REQUEST = 1888;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnSave = findViewById(R.id.btnSave);
        btnLoad = findViewById(R.id.btnLoad);
        etName = findViewById(R.id.etName);
        photoButton = findViewById(R.id.photoButton);
        mainImageView = findViewById(R.id.mainImageView);

        View.OnClickListener photoButtonListener = this::photoButtonClicked;
        View.OnClickListener btnSaveListener = this::btnSaveClicked;
        View.OnClickListener btnLoadListener = this::btnLoadClicked;

        btnSave.setOnClickListener(btnSaveListener);
        btnLoad.setOnClickListener(btnLoadListener);
        photoButton.setOnClickListener(photoButtonListener);

        etName.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

            }

            @Override
            public void afterTextChanged(Editable s) {
                dumpText();
            }
        });
        loadData();


    }

    public void btnSaveClicked(View v) {
        dumpText();
    }

    public void btnLoadClicked(View v) {
        loadData();
    }

    public void loadData() {
        SharedPreferences pref = getPreferences(MODE_PRIVATE);
        String name = pref.getString("name", "");
        etName.setText(name);


        String previouslyEncodedImage = pref.getString("image_data", "");

        if(!previouslyEncodedImage.equalsIgnoreCase("") ){
            byte[] b = Base64.decode(previouslyEncodedImage, Base64.DEFAULT);
            Bitmap bitmap = BitmapFactory.decodeByteArray(b, 0, b.length);
            mainImageView.setImageBitmap(bitmap);
        }
    }


    public void dumpImage(){
        BitmapDrawable drawable = (BitmapDrawable) mainImageView.getDrawable();
        Bitmap realImage = drawable.getBitmap();
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        realImage.compress(Bitmap.CompressFormat.JPEG, 100, baos);
        byte[] b = baos.toByteArray();
        String encodedImage = Base64.encodeToString(b, Base64.DEFAULT);


        SharedPreferences pref = getPreferences(MODE_PRIVATE);
        SharedPreferences.Editor ed = pref.edit();
        ed.putString("image_data", encodedImage);
        ed.apply();
    }


    public void dumpText() {

        SharedPreferences pref = getPreferences(MODE_PRIVATE);
        SharedPreferences.Editor ed = pref.edit();
        String name = etName.getText().toString();
        ed.putString("name", name);
        ed.apply();
    }

    public void photoButtonClicked(View v) {
        Intent cameraIntent = new Intent(android.provider.MediaStore.ACTION_IMAGE_CAPTURE);
        startActivityForResult(cameraIntent, CAMERA_REQUEST);
    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == CAMERA_REQUEST && resultCode == Activity.RESULT_OK) {
            Bitmap photo = (Bitmap) data.getExtras().get("data");
            mainImageView.setImageBitmap(photo);
            dumpImage();
        }
    }
}