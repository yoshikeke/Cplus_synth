this.puyoStatus.top+= ConfigplayerFallingSpeed;
this.moveDestination = ( x + cx)*Config.puyoImWidth;
return'rotating';
checkSequentialPuyo(dx,dy);
for (let i = puyoImages.lenght - 1 ; i >= 0;i --){
    const j = Math.floor(Math.random()*(i+1));
    [this.puyoImages[i],this.puyoImages[j]]=[this.puyoImages[j],this.puyoImages[i]];
}