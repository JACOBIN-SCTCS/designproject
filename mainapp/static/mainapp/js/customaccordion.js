var accordions=document.getElementsByClassName("customaccordion");
for (var i=0 ;i<accordions.length;i++)
{
    accordions[i].onclick = function(){
        this.classList.toggle('is_open');
        var content = this.nextElementSibling;
        if(content.style.maxHeight){
            content.style.maxHeight=null;
        }
        else{
            content.style.maxHeight=content.scrollHeight + "px";

        }
    }
}