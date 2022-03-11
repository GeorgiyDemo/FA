package com.demka.md23;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class MainActivity extends Activity {
    private static final int CAMERA_REQUEST = 1888;
    ImageView mainImageView;
    Button cameraButton;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mainImageView = findViewById(R.id.mainImageView);
        cameraButton = findViewById(R.id.cameraButton);
        View.OnClickListener cameraButtonListener = this::cameraButtonClicked;
        cameraButton.setOnClickListener(cameraButtonListener);
    }

    public void cameraButtonClicked(View v) {
        Intent cameraIntent = new Intent(android.provider.MediaStore.ACTION_IMAGE_CAPTURE);
        startActivityForResult(cameraIntent, CAMERA_REQUEST);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == CAMERA_REQUEST && resultCode == Activity.RESULT_OK) {
            Bitmap photo = (Bitmap) data.getExtras().get("data");
            mainImageView.setImageBitmap(photo);
        }
    }
}