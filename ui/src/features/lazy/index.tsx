import React, { Suspense, FC } from 'react';

interface LazyPropTypes {
  children: JSX.Element;
}

const Lazy: FC<LazyPropTypes> = ({ children }) => {
  return <Suspense>{children}</Suspense>;
};

export default Lazy;
