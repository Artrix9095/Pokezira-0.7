

function update() {
  if( bLoading ) {
    if( ImageResourceLoadedCount == screenResources.length )
      if( charsetLoadedCount == charsets.length )
        if( mapLoadedCount == 2 ) 
          if( bMapEventsLoaded && bMapDataLoaded ) {
            bLoading = false;
            mapWidth = mapAbove.width;
            mapHeight = mapAbove.height;
            
            clearInterval(gameInterval);
            gameInterval = setInterval(function() {
              update();
              draw();
            }, 50);
            
          }
  } else {
    
    if( bConnected ) {
      updateTick++;
      if( updateTick > 10 ) {
        
        var sendStr = "";
        
        var running = "0";
        if( keyState.btn2 )
          running  = "1";
        
        
        if( tagAlong != "" && follower != null) {
          sendStr = "/update^" + mapID +"^"  + userEvent.mapPosition.X +"^"  + userEvent.mapPosition.Y +"^"  + userEvent.direction +"^"  + userEvent.stepAnimation + "^" + running + "^"  + (bInBattle ? "1" : "0") + "^"  + tagAlong +"^"  + follower.mapPosition.X +"^"  + (follower.mapPosition.Y-2) +"^"  + follower.direction +"^"  + follower.stepAnimation + "^" + running +"^\r\n\r\n";

        } else {
          sendStr = "/update^" + mapID +"^"  + userEvent.mapPosition.X +"^"  + userEvent.mapPosition.Y +"^"  + userEvent.direction +"^"  + userEvent.stepAnimation + "^" + running + "^"  + (bInBattle ? "1" : "0") + "\r\n\r\n";
        }
        ws.send(sendStr);
        updateTick = 0;
      }
    }
    
    if( activeScript.length > 0 ) {
      scriptUpdate();
    } else if( bInBattle ) {
      battleUpdate();
    } else {
      //Process input and movement.
      if( activeScript.length == 0 ) {
        if( userEvent.moveQueue.length == 0 ) {
          if( keyState.up ) {
            userEvent.addMoveQueue("Up");
          } else if( keyState.down ) {
            userEvent.addMoveQueue("Down");
          } else if( keyState.left ) {
            userEvent.addMoveQueue("Left");
          } else if( keyState.right ) {
            userEvent.addMoveQueue("Right");
          }
        }
      }