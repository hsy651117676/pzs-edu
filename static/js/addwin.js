
function addwin(mytitle,urls)
{
  $('#mywindows').dialog({
    title: mytitle,
    width: 800,
    height: 400,
    closed: false,
    cache: false,
    href:urls,
    maximizable:true,
    modal: true
  });

}
