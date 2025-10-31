<ul>
  {% for post in site.posts %}
    <div>
      <a href="{{ post.url }}"><h2>{{ post.title }}</h2></a>
      <p></p>{{ excerpt }}</p>
    </div>
  {% endfor %}
</ul>
