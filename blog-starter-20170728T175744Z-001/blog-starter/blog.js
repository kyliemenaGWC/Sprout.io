class BlogEntry {
//name, blogText
constructor(name, blogText){
	this.name = name;
	this.blogText = blogText;
}
}



function addEntryToBlog() {
  //Create new blog entrya

  var authorName = document.getElementById("blogEntryName").value;
  var blogText = document.getElementById("blogEntryText").value;
  var blogEntry = new BlogEntry(authorName, blogText);
  //Add the new entry, name and date to the blog
  createBlogEntryElement(blogEntry);
  createFooterElement(blogEntry);

  //Clear the inputs
}

function createBlogEntryElement(blogEntry) {
	var div = document.createElement("div");
	div.className = "blogEntry";
	div.innerText =blogEntry.blogText

	var blogDetails = document.getElementById("blogDetails");
	blogDetails.appendChild(div)
	}

function createFooterElement(blogEntry) {
	var blogFooter = document.createElement("div");
	blogFooter.className = "blogDate";
	blogFooter.innerText = "by " +blogEntry.name + " on " + Date();


	var blogDetails = document.getElementById("blogDetails");
	blogDetails.appendChild(blogFooter);

}
