/**
 * NekoFX模块
 */
module cn.rmshadows.NekoFX {
	//exports Neko11;
	exports NekoFX;
	//exports resources;

	requires java.desktop;
	requires javafx.base;
	requires javafx.controls;
	requires javafx.fxml;
	requires transitive javafx.graphics;

	opens resources to javafx.fxml;
//	opens resources to javafx.graphics;
}
