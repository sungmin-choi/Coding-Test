function Profile() {
  const foo = useAsyncValue(() => {
    return fetchFoo();
  }); // 비동기처리를 리액트 훅 으로 작성.

  if (foo.error) return <p>실패</p>;
  if (!foo.data) return <p>데이터 불러오는 중...</p>;
  return <div>{foo.data.name}님 안녕하세요.</div>;
}
