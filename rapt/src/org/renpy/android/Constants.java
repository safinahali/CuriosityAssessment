package org.renpy.android;

public class Constants {

	// Used by the google play store.
	public static String PLAY_BASE64_PUBLIC_KEY = "CHANGE_THIS";
    public static byte[] PLAY_SALT = new byte[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 };

    // Used by the expansion downloader.
    public static int fileVersion = 0;
    public static int fileSize = 0;

    // Used by the in-app purchasing code.
    public static String store = "none";
}
